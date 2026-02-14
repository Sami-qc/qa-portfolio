# SauceDemo - Test Scenarios

## TS-001: Successful login and view products
- User logs in with valid credentials
- Products page loads correctly

## TS-002: Invalid login attempt
- User enters invalid password
- Error message appears and user stays on login page

## TS-003: Add item to cart and verify cart
- User adds a product from Products page
- Cart shows correct item details (name, price, quantity)

## TS-004: Remove item from cart
- Cart contains at least one item
- User removes item and cart updates correctly

## TS-005: Start checkout flow
- User has items in cart
- User clicks Checkout and checkout information page opens

## TS-006: Sorting and navigation consistency
- User applies sorting (Price low to high)
- Opens product details and returns
- Sorting should remain applied after navigation

## TS-007: Checkout attempt with empty cart (negative)
- Cart is empty
- User attempts to proceed to checkout
- System should block the flow or show a clear message
