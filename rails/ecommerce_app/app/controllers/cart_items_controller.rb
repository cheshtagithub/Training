class CartItemsController < ApplicationController
  def index
    @cart_items = CartItem.where(user_id: 1).includes(:product)
  end
  
  def create
    # Step 1: check product exists
    product = Product.find_by(id: params[:product_id])

    unless product
      redirect_to products_path, alert: "Product not found"
      return
    end

    # Step 2: find existing cart item
    cart_item = CartItem.find_by(
      product_id: product.id,
      user_id: 1
    )

    # Step 3: update or create
    if cart_item
      cart_item.quantity += 1
    else
      cart_item = CartItem.new(
        product_id: product.id,
        user_id: 1,
        quantity: 1
      )
    end

    # Step 4: save with handling
    if cart_item.save
      redirect_to cart_items_path, notice: "Item added to cart"
    else
      redirect_to cart_items_path, alert: "Something went wrong"
    end

  end

  def update
    cart_item = CartItem.find_by(id: params[:id], user_id: 1)

    # Step 0: safety check
    unless cart_item
      redirect_to cart_items_path, alert: "Item not found"
      return
    end

    # Step 1: update quantity
    if params[:type] == "increase"
      cart_item.quantity += 1

    elsif params[:type] == "decrease"
      if cart_item.quantity > 1
        cart_item.quantity -= 1
      else
        cart_item.destroy
        redirect_to cart_items_path, notice: "Item removed"
        return
      end
    end

    # Step 2: save
    if cart_item.save
      redirect_to cart_items_path, notice: "Cart updated"
    else
      redirect_to cart_items_path, alert: "Update failed"
    end
  end

  def destroy
    cart_item = CartItem.find_by(id: params[:id], user_id: 1)

    # Step 0: safety check
    unless cart_item
      redirect_to cart_items_path, alert: "Item not found"
      return
    end

    cart_item.destroy 
    redirect_to cart_items_path, notice: "Item removed"
  end
end
