MIN_CAPITAL = 5_000_000

class Bank:
    def __init__(self, name: str, stakeholders: list[str], capital: int) -> None:
        if capital < MIN_CAPITAL:
            raise ValueError("Too low capital amount")
        
        self.name = f'VAT {name.upper()}'
        self.stakeholders = stakeholders
        self.capital = capital

        pass