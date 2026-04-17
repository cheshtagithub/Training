class CreateJoinTableUsersProducts < ActiveRecord::Migration[8.1]
  def change
    create_join_table :users, :products
  end
end
