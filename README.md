# Hear

Hear is a convenience wrapper for the OpenAI Whisper API on Linux systems.

## Installation

While we are working on a proper package, you can install it by cloning the repository and running the following command:

    python setup.py install

The setup script will create a directory in your ~/.config directory and a sample api_key file in it. You will need to replace that with your API key before you can use the program.

Also, a symbolic link will be created in ~/.local/bin, so you can run the program from anywhere.

## Dependencies

The program relies on xdotool for sending keystrokes to the window manager. It also relies on the following python packages:

* openai
* argparse

## Usage

Running hear from the command line will start the background listening process. Running it again will stop the process and send the recorded message to the OpenAI API.

Use __hear -a__ to abort the recording process without sending the message to the API.

## Voice syntax

Words said after "beep" will be interpreted as commands. For instance, instead of writing "enter", the Return key will be pressed.

## Suggestions

No matter your DE/WM, I suggest setting a keybinding to run hear in the background, and possibly another one that runs hear -a. The best thing would be a 'press to talk' keybinding, but I haven't figured that out yet in my environment.

While we work on externalizing the config, there are some tweaks you can do to the code:

- Changing the command keyword (safeword, if you will) if you feel like going "BEEP" out loud is weird.
- Changing the recording limit. The default is 60.
- Changing the model used for the API call. The default is whisper-1.
- Changing the expected language. The default is ('en'). While it might be caused by my non-native English, I have found the API sometimes returning text in Russian or Japanese when language is not enforced. For those of us out there writing in more than one language, I guess we will just have to hold on, as the API accepts only one.

## Contributing

yes please

## License

This project is licensed under the MIT License - see the LICENSE file for details.