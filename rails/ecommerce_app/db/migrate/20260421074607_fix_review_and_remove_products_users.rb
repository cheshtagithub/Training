class FixReviewAndRemoveProductsUsers < ActiveRecord::Migration[8.1]
  def change
    remove_column :reviews, :product_references, :string

    add_reference :reviews, :product, null: false, foreign_key: true

    drop_table :products_users
  end
end
