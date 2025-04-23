:: Copyright (c) 2025 Tanush Chugh
:: This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
:: If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

@echo off
echo Cloning the repository...
git clone https://github.com/TanushChugh19/Octahedron-AI.git
cd Octahedron-AI

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete! You can now run the bot.
