class CartItem < ApplicationRecord
  belongs_to :user
  belongs_to :product

  validates :quantity, presence: true, numericality: { greater_than_or_equal_to: 0 }
  
  validates :user_id, presence: true

  validates :product_id, presence: true
  
  validates :product_id, uniqueness: { scope: :user_id, message: "already added to cart" }
end
