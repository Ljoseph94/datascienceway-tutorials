# XLOOKUP formulas from the tutorial

Open `xlookup_practice.xlsx` (Excel 365/2021+) — the formulas below are already entered next to the sample data. `products.csv` and `commission_bands.csv` hold the same data.

```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

```
     A           B                 C           D
1    Code        Product           Category    Price
2    P-101       Desk lamp         Lighting    24.99
3    P-102       Office chair      Furniture   149.00
4    P-103       Monitor arm       Accessories 39.50
5    P-104       Standing desk     Furniture   329.00
6    P-105       LED strip         Lighting    17.25
```

```
=XLOOKUP(F2, A2:A6, B2:B6)
```

```
=XLOOKUP(F2, A2:A6, B2:B6, "Code not found")
```

```
=XLOOKUP(F4, B2:B6, A2:A6, "Not found")
```

```
=XLOOKUP(F2, Products[Code], Products[Product], "Code not found")
```

```
     I              J
1    Sales from     Commission
2    0              0%
3    10000          3%
4    25000          5%
5    50000          7%
```

```
=XLOOKUP(L2, I2:I5, J2:J5, , -1)
```

```
=XLOOKUP("*desk*", B2:B6, B2:B6, "No match", 2)
```

```
=XLOOKUP("Furniture", C2:C6, B2:B6, , 0, -1)
```

```
=XLOOKUP(F2, A2:A6, B2:D6)
```

```
=XLOOKUP(F2, A2:A6, XLOOKUP(F8, A1:D1, A2:D6))
```
