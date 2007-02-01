/***************************************************************************
 *   Copyright (C) 2006 by FThauer FHammer   *
 *   f.thauer@web.de   *
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 *   This program is distributed in the hope that it will be useful,       *
 *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
 *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
 *   GNU General Public License for more details.                          *
 *                                                                         *
 *   You should have received a copy of the GNU General Public License     *
 *   along with this program; if not, write to the                         *
 *   Free Software Foundation, Inc.,                                       *
 *   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             *
 ***************************************************************************/
#ifndef SETTINGSDIALOGIMPL_H
#define SETTINGSDIALOGIMPL_H

#include "ui_settingsdialog.h"

#include <QtCore>
#include <QtGui>


class settingsDialogImpl: public QDialog, public Ui::settingsDialog {
Q_OBJECT
public:
    settingsDialogImpl(QWidget *parent = 0);

	void setPlayerNickIsChanged(bool theValue){ playerNickIsChanged = theValue;}
	bool getPlayerNickIsChanged() const{ return playerNickIsChanged;}

public slots:

	void isAccepted();
	void playerNickChanged() { setPlayerNickIsChanged(TRUE); };
	void setFlipsidePicFileName();

private:
	
	bool playerNickIsChanged;

};

#endif
