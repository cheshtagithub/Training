class Product < ApplicationRecord
  belongs_to :category
  has_many :order_items
  has_many :orders, through: :order_items
  has_many :cart_items
  has_many :users, through: :cart_items
  has_many :reviews
  
  validates :name, presence: true
  
  validates :price, presence: true, numericality: { greater_than: 0 }
  
  validates :stock, presence: true, numericality: { greater_than_or_equal_to: 0 }

  validates :category_id, presence: true

  before_create :set_default_stock
  private
  def set_default_stock
    self.stock ||= 0
  end
end
