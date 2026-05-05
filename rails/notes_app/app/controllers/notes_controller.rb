class NotesController < ApplicationController
  before_action :authenticate_user!
  before_action :set_note, only: [:show, :edit, :update, :destroy]

  def index
    if params[:search].present?
      @notes = current_user.notes.where("title ILIKE ?", "%#{params[:search]}%").page(params[:page]).per(4)
      
    else
      @notes = current_user.notes.page(params[:page]).per(4)  
    end
  end
  
  def show
  end

  def new
    @note = current_user.notes.new
  end

  def create
    @note = current_user.notes.new(note_params)

    if @note.save
      redirect_to @note, notice: "Note created successfully"

    else
      render :new
    end
  end

  def edit
  end

  def update
    if @note.update(note_params)
      redirect_to @note, notice: "Note updated"
    else
      render :edit
    end
  end

  def destroy
    @note.destroy
    redirect_to notes_path, notice: "Note deleted"
  end

  private

  def set_note
    @note = current_user.notes.find(params[:id])
  end

  def note_params
    params.require(:note).permit(:title, :content)
  end
end
