class RemoveTitleFromReviews < ActiveRecord::Migration[8.1]
  def change
    remove_column :reviews, :title, :string
  end
end
