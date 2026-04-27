class Book < ApplicationRecord
  validates :title, presence: true
  validates :author, presence:true
  validates :price, presence: true, numericality: { greater_than: 0 }

  validates :description, length: { minimum: 10 }
  validates :genre, presence: true

  before_save :capitalize_title
  before_validation :set_default_genre

  private

  def capitalize_title
    self.title = title.titleize
  end

  def set_default_genre
    self.set_default_genre = "General" if genre.blank?    
  end
end
