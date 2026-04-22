class Expense < ApplicationRecord
  belongs_to :user
  belongs_to :category

  validates :amount, presence: true, numericality: { greater_than: 0 }
  validates :date, presence: true
  validates :description, presence: true

  scope :this_month, -> {
    where(date: Date.current.beginning_of_month..Date.current.end_of_month)
  }
  scope :for_user, ->(user_id) {
    where(user_id: user_id)
  }

  after_create :check_budget

  def check_budget
    budget = Budget.find_by(user_id: user_id, category_id: category_id)
    return unless budget

    total = user.expenses.for_user(user_id).this_month.where(category_id: category_id).sum(:amount)

    if total > budget.monthly_limit
      puts "⚠️ Budget exceeded for #{category.name}!"
    end
  end
end
