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

  def edit
    @task = current_user.tasks.find(params[:id])
  end

  def update
    @task = current_user.tasks.find(params[:id])

    if @task.update(task_params)
      redirect_to "/tasks", notice: "Task updated successfully"
    else
      render :edit, status: :unprocessable_entity
    end
  end

  def destroy
    task = current_user.tasks.find(params[:id])
    task.destroy
    redirect_to "/tasks", notice: "Task deleted"
  end

  private

  def task_params
    params.require(:task).permit(:title, :description, :status)
  end
end
