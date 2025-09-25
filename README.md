# DocPassGen
 Simple CLI password generator

## 🔹 Install

1. Clone git repo:

```bash
git clone https://github.com/yourusername/passgen.git
cd passgen
```

2. Install packages:

```bash
pip install -e .
```
---
## 🔹 Use

### Generate with print in CLI:

```bash
passgen --length 16 --symbols --digits --serv github
```

### Save in Json in ~/.pass.json:

```bash
passgen --length 16 --symbols --digits --serv github --json
```

---

## 🔹 Args

| Args    | Desc                       |
| ----------- | ------------------------------ |
| `--length`  | Length (default= 12)) |
| `--symbols` | Spec. Symbols true/false (default= true)          |
| `--digits`  | Digits true/false (default= true)                 |
| `--serv`    | Name of sites/apps       |
| `--json`    | Save in Json true/false (default= false)   |

---

## 🔹 Exmaple

```json
[
    {
        "servs": "github",
        "pass": "aB3!xY9$LpQ#"
    },
    {
        "servs": "gmail",
        "pass": "Kp7@zT4^QmL!"
    }
]
```

---

## 🔹 Dependencies

* Python >= 3.12
