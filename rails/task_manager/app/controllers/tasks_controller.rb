class TasksController < ApplicationController
  before_action :authenticate_user

  def index
    @tasks = current_user.tasks
  end

  def new
    @task = Task.new
  end

  def create
    @task = current_user.tasks.build(task_params)

    if @task.save
      redirect_to "/tasks", notices: "Task created successfully"
    
    else
      render :new, status: :unprocessable_entity  
    end
  end

  def destroy
    task = current_user.tasks.find(params[:id])
    task.destroy
    redirect_to "/tasks", notice: "Task deleted"
  end

  private

  def task_params
    params.requires(:task).permit(:title, description, :status)
  end
end
