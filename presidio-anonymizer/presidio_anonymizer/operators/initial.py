from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    def operate(self, text: str = None, params: Dict = None) -> str:
        if text is None:
            return text

        words = text.split()
        initials_parts = []

        for word in words:
            first_char = None
            for ch in word:
                if ch.isalnum():
                    first_char = ch.upper()
                    break

            if first_char:
                initials_parts.append(f"{first_char}.")

        return " ".join(initials_parts)


    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
