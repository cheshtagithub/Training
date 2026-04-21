class Coupon < ApplicationRecord
  validates :code, presence: true, uniqueness: true
    validates :discount, presence: true
end
