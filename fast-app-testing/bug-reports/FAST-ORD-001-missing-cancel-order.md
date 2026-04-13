# FAST-ORD-001 — Missing Cancel Order Option

## Bug Summary
Users cannot cancel an active order after placing it in the Fast app.

## Module
Orders / Current Orders / Order Details / Order Tracking

## Bug Type
Functional Bug / UX Issue / Business Logic Gap

## Severity
High

## Priority
High

## Environment
- Platform: Android mobile app
- Feature Area: Post-order flow

## Preconditions
1. User is logged in
2. User selects location
3. User places an order successfully
4. Order is still active

## Steps to Reproduce
1. Open the Fast app
2. Place an order successfully
3. Go to **Current Orders**
4. Open the active order
5. Review the order details and tracking screen

## Actual Result
The user can view order details, track the order, and contact support, but there is no **Cancel Order** option available.

## Expected Result
If the order is still in an allowed stage, the user should be able to see and use a **Cancel Order** action.

## Evidence
- GIF showing the full post-order flow
- Screenshots of:
  - order success screen
  - current orders screen
  - order details screen
  - order tracking screen

## Impact
- Poor user experience
- Higher support dependency
- Possible restaurant loss
- Unclear refund handling for online payments

## Notes
This issue appears to be a product and system gap, not only a UI issue, because the cancellation flow is missing entirely from the active order journey.
