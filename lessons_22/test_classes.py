from class_data import Bank, MIN_CAPITAL
import pytest

class TestBank:
    def test_bank_creation_to_low_capital(self):
        with pytest.raises(ValueError):
            bank = Bank("Test", ["Test"], MIN_CAPITAL-1)

    def test_bank_add_one_stakeholder(self):
        bank = Bank("Test", ["Test"], MIN_CAPITAL)
        bank.stakeholders.append("Ilon Mask")
        bank.capital += 1_000

        assert len(bank.stakeholders) == 2, f"Expected 2, but got {len(bank.stakeholders)}"
        assert bank.capital == MIN_CAPITAL + 1_000, f"Expected {MIN_CAPITAL + 1_000}, but got {bank.capital}"

    def test_bank_creation_name(self):
        bank = Bank("Test", ["Test"], MIN_CAPITAL)
        assert bank.name == "VAT TEST", f"Expected Test, but got {bank.name}"
