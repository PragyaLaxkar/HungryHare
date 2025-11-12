# Hungry Hare — Food Ordering CLI

A tiny command-line food ordering app for a fictional quick-serve restaurant, "Hungry Hare." The app is a single-file Python script that lets users browse a menu, add items to a cart, modify quantities, view the cart (tax included), and checkout from the terminal.

## Features

- Browse a simple menu with SKUs, names and prices
- Add, remove and modify item quantities in a cart
- View the cart subtotal including sales tax
- Checkout to display final total and a thank-you message

## Requirements

- Python 3.8+
- No external dependencies (pure Python standard library)

## Installation

No installation is required. Clone or download the repository and run the script with Python.

## Quick Start (run)

From the `food_ordering_app` directory run (PowerShell):

```powershell
python .\app.py
```

When the app starts you'll see a welcome message and a numbered action menu. Follow the prompts to add items to your cart and checkout.

## Usage (what to expect)

- Actions are selected by entering the action number (1–6)
- Menu SKUs are presented as simple numbers (1 for `sku1`, 2 for `sku2`, etc.)
- Quantities default to 1 when not provided or when a non-numeric value is entered
- Sales tax is applied automatically when viewing the cart or checking out

Example: Add 2 hamburgers

1. Choose action `1` (Add a new menu item to cart)
2. Enter SKU `1`
3. Enter quantity `2`

## Configuration

- Restaurant name: modify the `restaurant_name` variable in `app.py`
- Sales tax: change `sales_tax_rate` in `app.py` (default: `0.07`)
- Menu: edit the `menu` dictionary in `app.py` to add/remove items. Use keys like `"sku11"` for additional items and the app will display their numeric suffix.

## Project structure

- `app.py` — main application script (single-file CLI implementation)
- `README.md` — this file

Key functions in `app.py`:

- `display_menu()` — prints the menu
- `add_to_cart(parsed_sku, quantity=1)` — add or increment an item in the cart
- `remove_from_cart(parsed_sku)` — remove an item completely
- `modify_cart(parsed_sku, quantity)` — set a new quantity (or remove when 0)
- `view_cart()` — show items and tax-inclusive total
- `checkout()` — show final cart and exit
- `get_sku_and_quantity(...)` — helper to read and parse input
- `order_loop()` — main interactive loop

## Example session (abridged)

```
---------- Welcome to Hungry Hare ---------

***** Ordering Actions *****
(1) Add a new menu item to cart
(2) Remove an item from the cart
(3) Modify a cart item's quantity
(4) View cart
(5) Checkout
(6) Exit
Please enter the number of the action you want to take: 1

***** Here is the menu *****
(1) Hamburger: $6.51
(2) Cheeseburger: $7.75
...
Please enter the SKU number for the menu item you want to order: 1
Please enter the quantity you want to order [default is 1]: 2
Added 2 of Hamburger to the cart.
```

## Contributing

This is a small demo script. Contributions are welcome — open an issue or submit a pull request for bug fixes or small improvements (e.g., input validation, persistence, or tests).

## License

This project is provided as-is for learning/demo purposes. No license specified.

## Notes & next steps

- Consider adding automated tests and input validation for production use.
- Optionally persist orders to a file or add a simple web UI.
