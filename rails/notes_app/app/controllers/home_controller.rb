class HomeController < ApplicationController
  def index
    if user_signed_in?
      # later we will show notes here
    else
      redirect_to new_user_session_path
    end
  end
end
