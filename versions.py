from dataclasses import dataclass


@dataclass
class Version:
    commit: str
    sha256: str


versions = {
    "20200503": Version(
        commit='8434966ca401a2a48f6654d3cf4c7bc68ac5fa4b',
        sha256='1cf08f62a9d025dbe09508ae4a6eb7b53a5046e1e4c4550c237f490f12ecc439')
}
