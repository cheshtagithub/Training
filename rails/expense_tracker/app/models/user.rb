class User < ApplicationRecord
  has_many :expenses, dependent: :destroy
  has_many :budgets

  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
end
