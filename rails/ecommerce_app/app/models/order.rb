class Order < ApplicationRecord
  belongs_to :user
  has_many :order_items
  has_many :products, through: :order_items
  has_many :reviews

  validates :total_price, presence: true, numericality: { greater_than_or_equal_to: 0 }

  validates :user_id, presence: true

  before_save :calculate_total_price

  private

  def calculate_total_price
    self.total_price = order_items.sum do |item|
      item.quantity * item.product.price
    end
  end
end
