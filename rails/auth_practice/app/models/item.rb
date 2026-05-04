class Item < ApplicationRecord
  extend FriendlyId
  friendly_id :name, use: :slugged
  mount_uploader :image, ImageUploader
end
