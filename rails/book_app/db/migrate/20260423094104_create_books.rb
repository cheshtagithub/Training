class CreateBooks < ActiveRecord::Migration[8.1]
  def change
    create_table :books do |t|
      t.string :title
      t.string :author
      t.text :description
      t.decimal :price
      t.date :published_on
      t.string :genre

      t.timestamps
    end
  end
end
