class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  has_many :notes, dependent: :destroy
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  validates :email,
    format: { with: URI::MailTo::EMAIL_REGEXP, message: "must be valid email" }

  validates :password,
    format: {
      with: /\A(?=.*[a-zA-Z])(?=.*\d).{8,}\z/,
      message: "must be at least 8 characters, include letters and numbers"
    },
    if: -> { password.present? }  
end
