class TestJob
  include Sidekiq::Job

  def perform(name)
    Rails.logger.info "Hello #{name} from Sidekiq!"
  end
end
