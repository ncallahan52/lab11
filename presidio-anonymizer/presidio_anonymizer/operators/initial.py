from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType


class Initial(Operator):
    def operate(self, text: str = None, params: Dict = None) -> str:
        if text is None:
            return text

        words = text.split()
        results = []

        for word in words:
            prefix = ""
            first_alnum = None

            for ch in word:
                if first_alnum is None and ch.isalnum():
                    first_alnum = ch.upper()
                    break
                prefix += ch

            if first_alnum:
                results.append(f"{prefix}{first_alnum}.")
            else:
                results.append(prefix)

        return " ".join(results)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize
