/*============================================================================
 * User definition of physical properties.
 *============================================================================*/

/* VERS */

/*
  This file is part of code_saturne, a general-purpose CFD tool.

  Copyright (C) 1998-2022 EDF S.A.

  This program is free software; you can redistribute it and/or modify it under
  the terms of the GNU General Public License as published by the Free Software
  Foundation; either version 2 of the License, or (at your option) any later
  version.

  This program is distributed in the hope that it will be useful, but WITHOUT
  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
  details.

  You should have received a copy of the GNU General Public License along with
  this program; if not, write to the Free Software Foundation, Inc., 51 Franklin
  Street, Fifth Floor, Boston, MA 02110-1301, USA.
*/

/*----------------------------------------------------------------------------*/

#include "cs_defs.h"

/*----------------------------------------------------------------------------
 * Standard C library headers
 *----------------------------------------------------------------------------*/

#include <assert.h>
#include <math.h>
#include <string.h>

#if defined(HAVE_MPI)
#include <mpi.h>
#endif

/*----------------------------------------------------------------------------
 * PLE library headers
 *----------------------------------------------------------------------------*/

#include <ple_coupling.h>

/*----------------------------------------------------------------------------
 * Local headers
 *----------------------------------------------------------------------------*/

#include "cs_headers.h"

/*----------------------------------------------------------------------------*/

BEGIN_C_DECLS

/*----------------------------------------------------------------------------*/
/*!
 * \file cs_user_physical_properties.c
 *
 * \brief User definition of physical properties.
 */
/*----------------------------------------------------------------------------*/

/*============================================================================
 * User function definitions
 *============================================================================*/

/*----------------------------------------------------------------------------*/
/*!
 * \brief Function called at each time step to define physical properties.
 *
 * \param[in, out]  domain   pointer to a cs_domain_t structure
 */
/*----------------------------------------------------------------------------*/

void
cs_user_physical_properties(cs_domain_t   *domain)
{
  CS_NO_WARN_IF_UNUSED(domain);

  /* Check fields exists */
  if (CS_F_(rho) == NULL)
    bft_error(__FILE__, __LINE__, 0,_("error rho not variable\n"));

  const cs_lnum_t n_cells = cs_glob_mesh->n_cells;

  cs_real_t *cpro_rho = CS_F_(rho)->val;
  const cs_real_t *cvar_temp = CS_F_(t)->val;
  const cs_real_t *grav = cs_glob_physical_constants->gravity;

  const cs_real_t ro0 = cs_glob_fluid_properties->ro0;
  const cs_real_t cp0 = cs_glob_fluid_properties->cp0;
   const cs_real_t lambda0 = cs_glob_fluid_properties->lambda0;
  const cs_real_t viscl0 = cs_glob_fluid_properties->viscl0;

  /* Value of the imposed Rayleigh number */
  const cs_real_t Ra = 1.e6;

  /* The givens of the problem */
  const cs_real_t L = 1.0, T_hot = 303.15, T_cold = 293.15;
  const cs_real_t g = sqrt(cs_math_sq(grav[0]) + cs_math_sq(grav[1])
                    + cs_math_sq(grav[2]));

  const cs_real_t beta = lambda0 * viscl0 * Ra /
                         (cs_math_sq(ro0) * cp0 * g * pow(L,3) *
                          (T_hot - T_cold));

  /* Compute density in all cells */
  cs_real_t min_rho = 1.e15, max_rho = 0.;
  for (cs_lnum_t cell_id = 0; cell_id < n_cells; cell_id++) {
    const cs_real_t temp_cell = cvar_temp[cell_id];
    cpro_rho[cell_id] = ro0 * (1. - beta * (temp_cell - T_cold));
    min_rho = fmin(cpro_rho[cell_id], min_rho);
    max_rho = fmax(cpro_rho[cell_id], max_rho);
  }

  if (cs_glob_rank_id >= 0) {
    cs_parall_min(1, CS_REAL_TYPE, &min_rho);
    cs_parall_max(1, CS_REAL_TYPE, &max_rho);
  }

  bft_printf("min_rho %f max_rho %f\n", min_rho, max_rho);
}

/*----------------------------------------------------------------------------*/

END_C_DECLS
