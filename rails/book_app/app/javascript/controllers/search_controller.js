import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  connect() {
    this.timeout = null
  }

  input() {
    // clear previous timer
    clearTimeout(this.timeout)

    // set new timer
    this.timeout = setTimeout(() => {
      this.element.form.requestSubmit()
    }, 500) // 300ms delay
  }
}