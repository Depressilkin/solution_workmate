from model import ProductsList, parser

if __name__ == '__main__':
    execute = parser.parse_args()
    array = ProductsList()
    array.loader(execute.file)
    array.execute(execute.where, execute.aggregate)

        
