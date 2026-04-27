class OrdersController < ApplicationController
  before_action :authenticate_user
  
  def index
    @orders = current_user.orders.includes(:order_items)
  end

  def show
    @order = current_user.orders.find_by(id: params[:id])
  
    unless @order
      redirect_to orders_path, alert: "Order not found"
      return
    end
  
    @order_items = @order.order_items.includes(:product)
  end

  
  def create
    cart_items = current_user.cart_items.includes(:product)

    if cart_items.empty?
      redirect_to cart_items_path, alert: "Cart is empty"
      return
    end

    begin
      ActiveRecord::Base.transaction do
        order = current_user.orders.create!(total_price: 0)

        total = 0

        cart_items.each do |item|
          order.order_items.create!(
            product: item.product,
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