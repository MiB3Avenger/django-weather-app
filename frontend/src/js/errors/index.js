/**
 * Extending custom errors for our app.
 * Current implementation is using index.js as main file, but as the project gets larger,
 * we will have specific errors in seperate files.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 * @file @js/errors/index.js
 * @exports Error Multiple error classes are exported from this file.
 */

/**
 * Error: Type of toast is invalid. It should be one of the mentioned types:
 * "success", "warning" or "error"
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 */
export class InvalidToastTypeError extends Error {
    constructor(message) {
        super(message)
        this.name = "InvalidToastType"
    }
}

/**
 * Error: Message for toast is invalid. It shouldn't be empty.
 * 
 * @author Chinmay Nagrale
 * @version 0.1
 */
export class InvalidToastMessageError extends Error {
    constructor(message) {
        super(message)
        this.name = "InvalidToastMessage"
    }
}