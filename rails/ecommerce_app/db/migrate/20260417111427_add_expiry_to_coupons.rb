class AddExpiryToCoupons < ActiveRecord::Migration[8.1]
  def change
    add_column :coupons, :expiry_date, :date
  end
end
