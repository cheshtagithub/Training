class WelcomeEmailJob
  include Sidekiq::Job

  def perform(user_id)
    user = User.find(user_id)
    Rails.logger.info "Sending welcome email to #{user.email}"
  end
end
