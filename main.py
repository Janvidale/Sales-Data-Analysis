sales_data = [
    {"ProductID": 1, "ProductName": "Product A", "Category": "Category 1", "QuantitySold": 10,
"UnitPrice": 20},
    {"ProductID": 2, "ProductName": "Product B", "Category": "Category 1", "QuantitySold": 5,
"UnitPrice": 30},
    {"ProductID": 3, "ProductName": "Product C", "Category": "Category 2", "QuantitySold": 20,
"UnitPrice": 15},
    {"ProductID": 4, "ProductName": "Product D", "Category": "Category 2", "QuantitySold": 7,
"UnitPrice": 25},
    {"ProductID": 5, "ProductName": "Product E", "Category": "Category 3", "QuantitySold": 3,
"UnitPrice": 50}
]

class sale_data_analysis:
    def __init__(self):
        self.__salesdata =[]

    def load_data(self,data):
        self.__salesdata =data

    def calculate_sale(self):
        total_sale=0
        for i in self.__salesdata:
            total_sale +=i ["QuantitySold"]*i["UnitPrice"]
            return total_sale

    def calculate_average_sale(self):
        total_sale=0
        unit_sold=0
        for i in self.__salesdata:
            total_sale += i["Quantitysold"]*i["UnitPrice"]
            unit_sold += i["Quantitysold"]
        avg = total_sale/unit_sold
        return avg

    def best_selling_prodect(self):
        sale_amount=[]
        productname=[]
        for i in self.__salesdata :
            sale_amount.append(i["Quantitysold"]*i["UnitPrice"])
            productname.append(i["ProductName"])
            index = (sale_amount.index(max(sale_amount)))
            return productName[index]
        
sale=sale_data_analysis
sale.load_data(sales_data)



















