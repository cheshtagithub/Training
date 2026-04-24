class OrdersController < ApplicationController
  def index
    @orders = Order.where(user_id: 1).includes(:order_items)
  end

  def show
    @order = Order.find_by(id: params[:id], user_id: 1)
  
    unless @order
      redirect_to orders_path, alert: "Order not found"
      return
    end
  
    @order_items = @order.order_items.includes(:product)
  end

  
  def create
    cart_items = CartItem.where(user_id: 1).includes(:product)

    if cart_items.empty?
      redirect_to cart_items_path, alert: "Cart is empty"
      return
    end

    begin
      ActiveRecord::Base.transaction do
        order = Order.create!(user_id: 1, total_price: 0)

        total = 0

        cart_items.each do |item|
          OrderItem.create!(
            order_id: order.id,
            product_id: item.product_id,
            quantity: item.quantity
          )

          total += item.product.price * item.quantity
        end

        order.update!(total_price: total)

        cart_items.destroy_all
      end

      redirect_to orders_path, notice: "Order placed successfully"

    rescue => e
      Rails.logger.error("Order failed: #{e.message}")
      redirect_to cart_items_path, alert: "Order failed"
    end
  end
end
