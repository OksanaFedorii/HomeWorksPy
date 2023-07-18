import datetime


class DataEntry:
    def __init__(self, date: datetime.date, time: datetime.time, sku: str, warehouse: str, warehouse_cell_id: int,
                 operation: str, invoice: str, expiration_date: datetime.date, operation_cost: float, comment: str):
        self.date = date
        self.time = time
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = warehouse_cell_id
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = expiration_date
        self.operation_cost = operation_cost
        self.comment = comment


class FileProcessor:
    def __init__(self, processed_filename: str, process_directory: str):
        self.processed_filename = processed_filename
        self.process_directory = process_directory

