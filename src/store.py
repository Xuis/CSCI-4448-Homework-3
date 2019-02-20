# =============================================================================
# Store "has-a" Catalog
# Store "has-a" Customer 
# Store tracks Rentals (invoices) and Inventory
# =============================================================================


class Store:
    def __init__(self):
        self.name = "Tools 'r' Us"
        self.Ledger = []
        self.Income = 0.00
