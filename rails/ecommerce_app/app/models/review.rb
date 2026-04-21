class Review < ApplicationRecord
  belongs_to :user
  belongs_to :order
  belongs_to :product

  validates :rating, presence: true
end
