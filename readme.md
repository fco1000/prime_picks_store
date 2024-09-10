# PrimePicks

## Slogan: "Handpicked Just for You"

the site should have various categories

- electronics,
- clothes,
- shoes
  etc

admin

vendor admin

various payment forms e.g _mpesa, stripe_

# Django E-commerce Shoe Store Project Structure

## 1. Products Management

### Models

- `Category`
- `Brand`
- `Shoe`
- `ShoeVariant`
- `Review`
- `Vendor`

### Views

- `CategoryListView` - Lists all categories
- `CategoryDetailView` - Lists shoes within a category
- `ShoeDetailView` - Displays details of a specific shoe
- `ReviewListView` - Lists reviews for a shoe
- `AddReviewView` - Form to submit a review
- `VendorProductListView` - Lists all products from a vendor
- `VendorAddProductView` - Form to add a new shoe
- `VendorEditProductView` - Form to edit an existing shoe

### Templates

- `category_list.html`
- `category_detail.html`
- `shoe_detail.html`
- `review_list.html`
- `add_review.html`
- `vendor_product_list.html`
- `vendor_add_product.html`
- `vendor_edit_product.html`

---

## 2. Cart and Checkout

### Models

- `Cart`
- `CartItem`
- `Order`
- `OrderItem`
- `Payment`
- `Address`

### Views

- `CartView` - Displays items in the cart
- `AddToCartView` - Adds an item to the cart
- `RemoveFromCartView` - Removes an item from the cart
- `UpdateCartView` - Updates the cart, such as changing quantities
- `CheckoutView` - Handles the checkout process for registered users
- `GuestCheckoutView` - Handles the checkout process for guest users
- `OrderSummaryView` - Displays a summary of the order after checkout

### Templates

- `cart.html`
- `checkout.html`
- `guest_checkout.html`
- `order_summary.html`

---

## 3. Account Management

### Models

- `Customer`
- `Address`

### Views

- `LoginView` - Handles user login
- `SignupView` - Handles user registration
- `ProfileView` - Displays and updates user profile information
- `OrderHistoryView` - Lists all orders made by the customer
- `OrderDetailView` - Displays details of a specific order
- `AddressBookView` - Allows management of saved addresses

### Templates

- `login.html`
- `signup.html`
- `profile.html`
- `order_history.html`
- `order_detail.html`
- `address_book.html`

---

## 4. Vendor Management

### Models

- `Vendor`

### Views

- `VendorDashboardView` - Main dashboard for vendors
- `VendorOrderListView` - Lists orders for vendor products
- `VendorOrderDetailView` - Details of an order relevant to a vendor

### Templates

- `vendor_dashboard.html`
- `vendor_order_list.html`
- `vendor_order_detail.html`

---

## 5. Admin Management

### Models

- (Leverage Django’s built-in `User` and `Admin` models)

### Views

- `AdminDashboardView` - Main dashboard for admins
- `AdminOrderListView` - Lists all orders in the store
- `AdminOrderDetailView` - Detailed view of an order for admins
- `AdminProductManagementView` - Manages all products in the store
- `AdminUserManagementView` - Manages all users in the store
- `AdminVendorManagementView` - Manages vendors and their products
- `AdminUpdateDeliveryView` - Updates the delivery status for orders

### Templates

- `admin_dashboard.html`
- `admin_order_list.html`
- `admin_order_detail.html`
- `admin_product_management.html`
- `admin_user_management.html`
- `admin_vendor_management.html`
- `admin_update_delivery.html`

---

## 6. Delivery Management

### Models

- `Delivery`

### Views

- `TrackDeliveryView` - Allows customers to track their orders
- `AdminUpdateDeliveryView` - Admin updates the delivery status

### Templates

- `track_delivery.html`
- `admin_update_delivery.html`

---

## 7. Common/Base

### Models

- (N/A)

### Views

- (N/A)

### Templates

- `base.html`
- `base_vendor.html`
- `base_admin.html`
- `home.html`
- `search_results.html`
