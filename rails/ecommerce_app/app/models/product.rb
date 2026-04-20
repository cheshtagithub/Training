class Product < ApplicationRecord
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
