BENCHMARK = tpacf

CWD = $(shell pwd)
SRCDIR = src
OBJDIR = obj
BINDIR = bin
DATADIR = $(CWD)/../../benchmarks_data/$(BENCHMARK)

CUSRC = $(SRCDIR)/main.cu
CCSRC = $(wildcard $(SRCDIR)/*.cc)
CSRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(patsubst $(SRCDIR)/%.cu,$(OBJDIR)/%.o,$(CUSRC)) \
      $(patsubst $(SRCDIR)/%.cc,$(OBJDIR)/%.o,$(CCSRC)) \
      $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(CSRC))
BIN = $(BINDIR)/$(BENCHMARK)
DATA = $(DATADIR)Datapnts.1,$(DATADIR)/Randompnts.1,$(DATADIR)/Randompnts.2,$(DATADIR)/Randompnts.3,$(DATADIR)/Randompnts.4,$(DATADIR)/Randompnts.5,$(DATADIR)/Randompnts.6,$(DATADIR)/Randompnts.7,$(DATADIR)/Randompnts.8,$(DATADIR)/Randompnts.9,$(DATADIR)/Randompnts.10,$(DATADIR)/Randompnts.11,$(DATADIR)/Randompnts.12,$(DATADIR)/Randompnts.13,$(DATADIR)/Randompnts.14,$(DATADIR)/Randompnts.15,$(DATADIR)/Randompnts.16,$(DATADIR)/Randompnts.17,$(DATADIR)/Randompnts.18,$(DATADIR)/Randompnts.19,$(DATADIR)/Randompnts.20,$(DATADIR)/Randompnts.21,$(DATADIR)/Randompnts.22,$(DATADIR)/Randompnts.23,$(DATADIR)/Randompnts.24,$(DATADIR)/Randompnts.25,$(DATADIR)/Randompnts.26,$(DATADIR)/Randompnts.27,$(DATADIR)/Randompnts.28,$(DATADIR)/Randompnts.29,$(DATADIR)/Randompnts.30,$(DATADIR)/Randompnts.31,$(DATADIR)/Randompnts.32,$(DATADIR)/Randompnts.33,$(DATADIR)/Randompnts.34,$(DATADIR)/Randompnts.35,$(DATADIR)/Randompnts.36,$(DATADIR)/Randompnts.37,$(DATADIR)/Randompnts.38,$(DATADIR)/Randompnts.39,$(DATADIR)/Randompnts.40,$(DATADIR)/Randompnts.41,$(DATADIR)/Randompnts.42,$(DATADIR)/Randompnts.43,$(DATADIR)/Randompnts.44,$(DATADIR)/Randompnts.45,$(DATADIR)/Randompnts.46,$(DATADIR)/Randompnts.47,$(DATADIR)/Randompnts.48,$(DATADIR)/Randompnts.49,$(DATADIR)/Randompnts.50,$(DATADIR)/Randompnts.51,$(DATADIR)/Randompnts.52,$(DATADIR)/Randompnts.53,$(DATADIR)/Randompnts.54,$(DATADIR)/Randompnts.55,$(DATADIR)/Randompnts.56,$(DATADIR)/Randompnts.57,$(DATADIR)/Randompnts.58,$(DATADIR)/Randompnts.59,$(DATADIR)/Randompnts.60,$(DATADIR)/Randompnts.61,$(DATADIR)/Randompnts.62,$(DATADIR)/Randompnts.63,$(DATADIR)/Randompnts.64,$(DATADIR)/Randompnts.65,$(DATADIR)/Randompnts.66,$(DATADIR)/Randompnts.67,$(DATADIR)/Randompnts.68,$(DATADIR)/Randompnts.69,$(DATADIR)/Randompnts.70,$(DATADIR)/Randompnts.71,$(DATADIR)/Randompnts.72,$(DATADIR)/Randompnts.73,$(DATADIR)/Randompnts.74,$(DATADIR)/Randompnts.75,$(DATADIR)/Randompnts.76,$(DATADIR)/Randompnts.77,$(DATADIR)/Randompnts.78,$(DATADIR)/Randompnts.79,$(DATADIR)/Randompnts.80,$(DATADIR)/Randompnts.81,$(DATADIR)/Randompnts.82,$(DATADIR)/Randompnts.83,$(DATADIR)/Randompnts.84,$(DATADIR)/Randompnts.85,$(DATADIR)/Randompnts.86,$(DATADIR)/Randompnts.87,$(DATADIR)/Randompnts.88,$(DATADIR)/Randompnts.89,$(DATADIR)/Randompnts.90,$(DATADIR)/Randompnts.91,$(DATADIR)/Randompnts.92,$(DATADIR)/Randompnts.93,$(DATADIR)/Randompnts.94,$(DATADIR)/Randompnts.95,$(DATADIR)/Randompnts.96,$(DATADIR)/Randompnts.97,$(DATADIR)/Randompnts.98,$(DATADIR)/Randompnts.99,$(DATADIR)/Randompnts.100
CMD = ./$(BENCHMARK) -i $(DATA) -o tpacf.out -- -n 100 -p 487 | tee sim.out
CMD1 = PTX_SIM_MODE_FUNC=1 $(CMD)
CMD2 = $(CMD)

INC = -I$(SRCDIR)
NVFLAGS = -arch sm_20 $(INC)

all: makedir $(BIN)

include ../common.mk

