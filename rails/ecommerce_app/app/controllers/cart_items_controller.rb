class CartItemsController < ApplicationController
  before_action :authenticate_user
  
  def index
    @cart_items = current_user.cart_items.includes(:product)
  end
  
  def create
    product = Product.find_by(id: params[:product_id])

    unless product
      redirect_to products_path, alert: "Product not found"
      return
    end

    cart_item = current_user.cart_items.find_by(product_id: product.id)

    if cart_item
      cart_item.quantity += 1
    else
      cart_item = current_user.cart_items.new(
        product: product,
        quantity: 1
      )
    end

    if cart_item.save
      redirect_to cart_items_path, notice: "Item added to cart"
    else
      redirect_to cart_items_path, alert: "Something went wrong"
    end
  end

  def update
    cart_item = current_user.cart_items.find_by(id: params[:id])

    unless cart_item
      redirect_to cart_items_path, alert: "Item not found"
      return
    end

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

    if cart_item.save
      redirect_to cart_items_path, notice: "Cart updated"
    else
      redirect_to cart_items_path, alert: "Update failed"
    end
  end

  def destroy
    cart_item = current_user.cart_items.find_by(id: params[:id])

    unless cart_item
      redirect_to cart_items_path, alert: "Item not found"
      return
    end

    cart_item.destroy 
    redirect_to cart_items_path, notice: "Item removed"
  end
end