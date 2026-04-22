class Budget < ApplicationRecord
  belongs_to :category
  belongs_to :user

  validates :monthly_limit, presence: true, numericality: { greater_than: 0 }
  validates :category_id, uniqueness: { scope: :user_id, message: "budget already set for this category" }
end
