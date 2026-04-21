class User < ApplicationRecord
  has_many :orders
  has_many :cart_items
  has_many :products, through: :cart_items
  has_many :reviews

  validates :name, presence: true, length: { minimum: 2 }

  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }

  before_save :downcase_email
  private

  def downcase_email
    self.email = email.downcase
  end
end
