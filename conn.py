import csv
import happybase
import time

batch_size = 1000
host = "0.0.0.0"
file_path = "acervo.csv"
namespace = "sample_data"
row_count = 0
start_time = time.time()
table_name = "acervo"


def connect_to_hbase():
    """ Faz a conexao com o servidor HBase
    """
    conn = happybase.Connection(host = host,
        table_prefix = namespace,
        table_prefix_separator = ":")
    conn.open()
    table = conn.table(table_name)
    batch = table.batch(batch_size = batch_size)
    return conn, batch


def insert_row(batch, row):
    """ Insere linhas no HBase
    Linhas seguem o seguinte schema
        [ id_exemplar, codigo_barras, colecao, biblioteca, status_material, localizacao, registro_sistema ]
    """
    batch.put(row[0], { "data:cod": row[1], "data:col": row[2], "data:bibl": row[3],
        "data:status": row[4], "data:local": row[5], "data:reg": row[6]})


def read_csv():
    csvfile = open(file_path, "r")
    csvreader = csv.reader(csvfile)
    return csvreader, csvfile


conn, batch = connect_to_hbase()
print (("Conectado ao HBase. nome da tabela: %s, tamanho do batch: %i") % (table_name, batch_size))
csvreader, csvfile = read_csv()
print (("Conectado ao arquivo. Nome: %s") % (file_path))

try:
    for row in csvreader:
        row_count += 1
        if row_count == 1:
            pass
        else:
            insert_row(batch, row)

    batch.send()
finally:
    csvfile.close()
    conn.close()

duration = time.time() - start_time
print (("Fim. Contagem de linhas: %i, duração: %.3f s") % (row_count, duration))