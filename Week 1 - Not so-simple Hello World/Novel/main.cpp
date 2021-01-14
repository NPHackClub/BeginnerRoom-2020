// Not Python
// Good luck linking SFML

#include <SFML/Graphics.hpp>

using namespace sf;

int main()
{
    VideoMode vm(600, 600);

    RenderWindow window(vm, "Esc to quit", Style::Default);
    window.setFramerateLimit(60);

    Text message;

    Font font;
    font.loadFromFile("fonts/Roboto-Regular.ttf");
    message.setFont(font);
    message.setString("Hello World");
    message.setCharacterSize(100);
    message.setFillColor(Color::White);

    // Main Loop
    while (window.isOpen())
    {
        // Input
        if (Keyboard::isKeyPressed(Keyboard::Escape))
        {
            window.close();
        }

        // Update
        FloatRect textRect = message.getLocalBounds();
        message.setOrigin(textRect.left + textRect.width / 2.0f, textRect.top + textRect.height / 2.0f);
        message.setPosition(600 / 2.0f, 600 / 2.0f);

        // Draw
        window.clear(Color::Black);
        window.draw(message);
        window.display();
    }


    return 0;
}