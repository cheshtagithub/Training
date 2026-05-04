class AddImageToItems < ActiveRecord::Migration[8.1]
  def change
    add_column :items, :image, :string
  end
end
